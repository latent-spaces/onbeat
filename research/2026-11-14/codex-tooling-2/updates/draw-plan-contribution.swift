import AppKit
let width = 1080
let height = 1350
let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
let context = NSGraphicsContext(bitmapImageRep: bitmap)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = context
NSColor(calibratedRed: 0.07, green: 0.10, blue: 0.15, alpha: 1).setFill()
NSRect(x: 0, y: 0, width: width, height: height).fill()
func text(_ value: String, _ y: CGFloat, _ size: CGFloat, _ color: NSColor, _ bold: Bool = false) {
 let style = NSMutableParagraphStyle()
 style.lineBreakMode = .byWordWrapping
 let font = bold ? NSFont.boldSystemFont(ofSize: size) : NSFont.systemFont(ofSize: size)
 (value as NSString).draw(in: NSRect(x: 82, y: y, width: 916, height: 260), withAttributes: [.font: font, .foregroundColor: color, .paragraphStyle: style])
}
let white = NSColor.white
let mint = NSColor(calibratedRed: 0.47, green: 0.91, blue: 0.72, alpha: 1)
text("PLAN CONTRIBUTION  /  14 NOV 2026", 1055, 25, mint, true)
text("Prove the path.\nThen share the reel.", 785, 76, white, true)
text("Two pilot journeys before launch", 625, 46, mint, true)
text("Agent user + CLI user → first MP4", 505, 39, white)
text("Owner actions sent to the plan editor", 415, 34, white)
text("Next: review the single plan PR", 170, 42, mint, true)
text("Research only · no launch or merge", 75, 26, white)
NSGraphicsContext.restoreGraphicsState()
let output = bitmap.representation(using: .png, properties: [:])!
try output.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
