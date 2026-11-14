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
text("PIXELLE-VIDEO", 1055, 25, mint, true)
text("Package first.\nAnnouncement later.", 785, 76, white, true)
text("Nov 9 → Nov 18, 2025", 625, 46, mint, true)
text("Windows bundle → project X post", 505, 39, white)
text("Primary sources · star causes unknown", 415, 34, white)
text("Next: link both in shared report", 170, 42, mint, true)
text("Research only · no launch or merge", 75, 26, white)
NSGraphicsContext.restoreGraphicsState()
let output = bitmap.representation(using: .png, properties: [:])!
try output.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
